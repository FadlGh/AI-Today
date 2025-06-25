import { useEffect, useState } from "react";

export default function Home() {
  const [msg, setMsg] = useState("");

  const backendUrl = "https://ai-today-bqpb.onrender.com";

  useEffect(() => {
    fetch(`${backendUrl}/api/test-supabase`)
      .then((res) => res.json())
      .then((data) => {
        if (data.data) {
          setMsg(JSON.stringify(data.data, null, 2));
        } else if (data.error) {
          setMsg(`Error: ${data.error}`);
        } else {
          setMsg("No data received");
        }
      })
      .catch(() => setMsg("Failed to reach backend"));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Today Frontend</h1>
      <pre>{msg}</pre>
    </div>
  );
}
