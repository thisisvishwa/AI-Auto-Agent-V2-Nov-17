```javascript
import dynamic from 'next/dynamic';
import { useEffect, useState } from 'react';

// Dynamic import for performance optimization
const AIComponent = dynamic(() => import('../components/AIComponent'), {
  ssr: false,
});

const NFTComponent = dynamic(() => import('../components/NFTComponent'), {
  ssr: false,
});

// Caching frequently accessed data
let cache = {};

function getCachedData(key) {
  return cache[key];
}

function setCachedData(key, data) {
  cache[key] = data;
}

export default function PerformanceOptimizedPage() {
  const [aiData, setAIData] = useState(getCachedData('aiData') || {});
  const [nftData, setNFTData] = useState(getCachedData('nftData') || {});

  useEffect(() => {
    if (!getCachedData('aiData')) {
      fetch('/api/aiData')
        .then((response) => response.json())
        .then((data) => {
          setAIData(data);
          setCachedData('aiData', data);
        });
    }

    if (!getCachedData('nftData')) {
      fetch('/api/nftData')
        .then((response) => response.json())
        .then((data) => {
          setNFTData(data);
          setCachedData('nftData', data);
        });
    }
  }, []);

  return (
    <div>
      <AIComponent data={aiData} />
      <NFTComponent data={nftData} />
    </div>
  );
}
```