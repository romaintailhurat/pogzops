import { Fragment, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, getAllLocalStorageItems, getRefValue, isTrue, preventDefault, processEvent, refs, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Box, Button, Grid, GridItem, Heading, HStack, Link, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import NextHead from "next/head"


export default function Component() {
  const [state, setState] = useState({"is_hydrated": false, "source": "demo", "source_env_name": "demo", "target_env_name": "prod-interne", "events": [{"name": "state.hydrate"}], "files": []})
  const [result, setResult] = useState({"state": null, "events": [], "final": true, "processing": false})
  const [notConnected, setNotConnected] = useState(false)
  const router = useRouter()
  const socket = useRef(null)
  const { isReady } = router
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Function to add new events to the event queue.
  const Event = (events, _e) => {
      preventDefault(_e);
      setState(state => ({
        ...state,
        events: [...state.events, ...events],
      }))
  }

  // Function to add new files to be uploaded.
  const File = files => setState(state => ({
    ...state,
    files,
  }))

  // Main event loop.
  useEffect(()=> {
    // Skip if the router is not ready.
    if (!isReady) {
      return;
    }

    // Initialize the websocket connection.
    if (!socket.current) {
      connect(socket, state, setState, result, setResult, router, ['websocket', 'polling'], setNotConnected)
    }

    // If we are not processing an event, process the next event.
    if (!result.processing) {
      processEvent(state, setState, result, setResult, router, socket.current)
    }

    // If there is a new result, update the state.
    if (result.state != null) {
      // Apply the new result to the state and the new events to the queue.
      setState(state => ({
        ...result.state,
        events: [...state.events, ...result.events],
      }))

      // Reset the result.
      setResult(result => ({
        state: null,
        events: [],
        final: true,
        processing: !result.final,
      }))

      // Process the next event.
      processEvent(state, setState, result, setResult, router, socket.current)
    }
  })

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => Event([E('state.hydrate', {})])
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
  <Fragment><Fragment>
  <VStack>
  <Heading size="4xl" sx={{"color": "#6A4C93"}}>
  {`Pogzops`}
</Heading>
  <Grid sx={{"width": "100%"}} templateColumns="repeat(3, 1fr)">
  <GridItem colSpan={1} rowSpan={1}>
  <VStack>
  <Heading size="lg">
  {`Envs`}
</Heading>
  <Text>
  {`Manage Pogues environments`}
</Text>
  <HStack>
  <Text>
  {`Current source env is:`}
</Text>
  <Text>
  {state.source_env_name}
</Text>
</HStack>
  <Link as={NextLink} href="/environments" sx={{"color": "#1982C4", "button": true}}>
  <Button>
  {`Go`}
</Button>
</Link>
</VStack>
</GridItem>
  <GridItem colSpan={1} rowSpan={1}>
  <Heading size="lg">
  {`Remote`}
</Heading>
</GridItem>
  <GridItem colSpan={1} rowSpan={1}>
  <Heading size="lg">
  {`Local`}
</Heading>
</GridItem>
</Grid>
</VStack>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content="A Reflex app." name="description"/>
  <meta content="favicon.ico" property="og:image"/>
</NextHead>
</Fragment>
    </Fragment>
  )
}
