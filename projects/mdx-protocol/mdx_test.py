from mdx import Channel


def test_encode_channel_to_bytes():
    mux_id = 1
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    channel = Channel(mux_id, data)

    expected = bytes([
        0x00, 0x01,  # version
        0x00, 0x00,  # checksum
        0x00, 0x00,  # reserved
        0x00, 0x01,  # mux_id
        0x00, 0x00, 0x00, 0x0A,  # length
        # data
        0x00, 0x01, 0x02, 0x03,
        0x04, 0x05, 0x06, 0x07,
        0x08, 0x09
    ])
    actual = bytes(channel)
    assert expected == actual


def test_decode_channel_from_bytes():
    data = bytes([
        0x00, 0x01,  # version
        0x00, 0x00,  # checksum
        0x00, 0x00,  # reserved
        0x00, 0x01,  # mux_id
        0x00, 0x00, 0x00, 0x0A,  # length
        # data
        0x00, 0x01, 0x02, 0x03,
        0x04, 0x05, 0x06, 0x07,
        0x08, 0x09
    ])
    expected = Channel(
        mux_id=1,
        data=bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    )
    actual = Channel.from_bytes(data)
    assert expected == actual
