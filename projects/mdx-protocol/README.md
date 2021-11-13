# MDX-Protocol
MDX-Protocol Stands for Multiplex/Demultiplex Protocol. The main intention
is to transparently multiplex arbitrary "data" channels.

## Goals
Provide a protocol which enables the usage of multiple communication channels through a single communication channel,
e.g. serial connection or network connection.

```shell
   SERVER                                             CLIENT
+------------+                                     +------------+
| n-channels | <-----> network-connection <----->  | n-channels |
+------------+                                     +------------+

   HOST                                               TARGET
+------------+                                     +------------+
| n-channels | <------> serial-connection  <-----> | n-channels |
+------------+                                     +------------+

...
```

## Previous works
* [IEN 90](https://www.rfc-editor.org/ien/ien90.txt)
* [RFC-1692](https://datatracker.ietf.org/doc/html/rfc1692)
* [WebMux Protocol](https://www.w3.org/Protocols/MUX/WD-mux-980722.html)

## Design Decisions
* **No Checksum of the data followed by the length field**

  * The responsibility of the data integrity of the de-/multiplexed
  data should be taken care of by the "protocol" (mechanism) used for the actual data exchange (e.g. UDP, TCP, ...).

* **Why not use IEN-90?**
 
    * The protocol must not know what data is transferred, within each channel.
    (This information highly depends on the usage [use case] and is therefore configuration dependent)

* **No assumption about the transport means of connection is made**

* **The purpose of protocol is multiplexing and demultiplexing, if e.g. a transport protocol, or reliable data tranfer is needed
  a protocol within the "data" section need to take care of this**


## Format
The Endianness used for all data within the header is BigEndian, unless 
stated otherwise.

```shell
0         16          32
|          |           |
------------------------  <-----+
| version  | checksum  |        |
------------------------        |
| reserved |   mux-id  |      Header
------------------------        |
|       length         |        |
------------------------  <-----+
|        data          |
------------------------
```

## Fields

| Field |  Size | Description |
|---|---|---|
| version  |  2 Byte | version of the used mdx-protocol |
| checksum |  2 Byte | checksum of the header (crc16, CCITT)|
| reserved |  2 Byte | reserved bytes |
| mux-id   |  2 Byte | identifier of the mux-channel the data is associated with |
| length   |  4 Byte | length of the data (in bytes) associated with this header |


## Examples
TBD

## Open Questions
* What happens if checksum error is detected?
    * **suggestion**: like IEN-90 ignore/drop "packet"/message
