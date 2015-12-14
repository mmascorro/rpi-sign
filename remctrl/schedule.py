import urllib,urllib2, base64, json, time, datetime, sys

baseUrl = "http://localhost:80/"
xbmcUrl = baseUrl + "jsonrpc"

def play(url, playlist):

    clearCmd = {
        "jsonrpc": "2.0",
        "method": "Playlist.Clear",
        "params": {
            "playlistid": 1
        },
        "id": 1
    }
    queueCmd = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Playlist.Add",
        "params": {
            "item": {
                "directory": playlist
            },
            "playlistid": 1
        }

    }
    playCmd = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Player.Open",
        "params": {
            "item": {
                "playlistid": 1,
                "position": 0
            },
            "options": {
                "repeat": "all"
            }
        }
    }
    fullCmd = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "GUI.SetFullscreen",
        "params": {
            "fullscreen": True
        }
    }
    send(url,clearCmd)
    send(url,queueCmd)
    send(url,playCmd)
    send(url,fullCmd)


def send(url,cmd):
    data = json.dumps(cmd)
    base64String = base64.encodestring("%s:%s" % ('xbmc','xbmc')).replace('\n','')
    request = urllib2.Request(url)
    request.add_header("Authorization", "Basic %s" % base64String)
    request.add_header("Content-Type", "application/json")
    request.add_data(data)
    result = urllib2.urlopen(request)
    print result.read()

if __name__ == "__main__":
    play(xbmcUrl, sys.argv[1])
