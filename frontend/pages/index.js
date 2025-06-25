import { useEffect, useState } from "react";

export default function Home() {
  const [msg, setMsg] = useState("");

  useEffect(() => {
    fetch("https://ai-today-bqpb.onrender.com/api/hello")
      .then((res) => res.json())
      .then((data) => setMsg(data.message))
      .catch((err) => {
        console.error(err);
        setMsg("Failed to reach backend");
      });
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Today Frontend</h1>
      <p>
        Backend says: <strong>{msg}</strong>
      </p>
    </div>
  );
}
