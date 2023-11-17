```javascript
import { useEffect, useState } from 'react';
import { w3cwebsocket as W3CWebSocket } from 'websocket';

const websocket_url = process.env.websocket_url;

const DataHandling = () => {
  const [aiData, setAiData] = useState(null);
  const [nftData, setNftData] = useState(null);
  const [userData, setUserData] = useState(null);
  const [realTimeData, setRealTimeData] = useState(null);

  useEffect(() => {
    const client = new W3CWebSocket(websocket_url);

    client.onopen = () => {
      console.log('WebSocket Client Connected');
    };

    client.onmessage = (message) => {
      const dataFromServer = JSON.parse(message.data);
      const { type, payload } = dataFromServer;

      switch (type) {
        case 'aiDataUpdate':
          setAiData(payload);
          break;
        case 'nftDataUpdate':
          setNftData(payload);
          break;
        case 'userDataUpdate':
          setUserData(payload);
          break;
        case 'realTimeDataUpdate':
          setRealTimeData(payload);
          break;
        default:
          break;
      }
    };
  }, []);

  return (
    <div>
      <div id="ai-data-display">{aiData && JSON.stringify(aiData)}</div>
      <div id="nft-data-display">{nftData && JSON.stringify(nftData)}</div>
      <div id="user-data-display">{userData && JSON.stringify(userData)}</div>
      <div id="real-time-data">{realTimeData && JSON.stringify(realTimeData)}</div>
    </div>
  );
};

export default DataHandling;
```