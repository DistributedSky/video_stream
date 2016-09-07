## DroneEmployee video streaming support

The aim of this is a spawn `streamer` (the executable that stream video)
according to smart contract logic. The code works with [Streaming.sol][1].

> For deploying smart contracts you can use [Aira deploy script][3]

The `streamer` is any bynary with two args:

 - video device (e.g. `/dev/video0`)
 - stream identifier (256bit hex, e.g. `4f66e...`) 

Sample video streamer: [bin/streamer_example.py][2]

[1]: https://github.com/DroneEmployee/contracts/blob/master/interface/Streaming.sol
[2]: https://github.com/DroneEmployee/video_stream/blob/master/bin/streamer_example.py
[3]: https://github.com/airalab/core/wiki/AIRA-Deploy

### Usage

    $ ./bin/streamd.sh              
    Usage: /usr/bin/node ./scripts/streamd.js -c [CONTRACT_ADDRESS] -e [STREAMING_BINARY]
    
    Options:
        --rpc  Web3 RPC provider                        [default: "http://localhost:8545"]
        -d     Video device to streaming                [default: "/dev/video0"]
        -c     Streaming contract address               [required]
        -e     Shell command to start streaming daemon  [required]

### Usage example

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/HB4BlSXatuY/0.jpg)](https://www.youtube.com/watch?v=HB4BlSXatuY)
