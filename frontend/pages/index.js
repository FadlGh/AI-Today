import { useState } from "react";

export default function Home() {
  const [title, setTitle] = useState("");
  const [summary, setSummary] = useState("");
  const [takes, setTakes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const backendUrl = "https://ai-today-bqpb.onrender.com";

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setTakes([]);

    try {
      const res = await fetch(`${backendUrl}/api/generate-takes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, summary }),
      });

      const data = await res.json();
      if (data.takes) {
        setTakes(data.takes);
      } else {
        setError(data.error || "Unknown error");
      }
    } catch (err) {
      setError("Failed to reach backend");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>📰 AI Today</h1>

      <form onSubmit={handleSubmit} style={{ marginBottom: 20 }}>
        <div>
          <label>Headline:</label>
          <br />
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            style={{ width: "100%", padding: "8px" }}
            required
          />
        </div>
        <div style={{ marginTop: 10 }}>
          <label>Summary:</label>
          <br />
          <textarea
            value={summary}
            onChange={(e) => setSummary(e.target.value)}
            style={{ width: "100%", height: 100, padding: "8px" }}
            required
          />
        </div>
        <button
          type="submit"
          style={{ marginTop: 10, padding: "10px 20px" }}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Takes"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {takes.length > 0 && (
        <div>
          <h2>Agent Takes</h2>
          {takes.map((take, index) => (
            <div
              key={index}
              style={{
                marginBottom: 20,
                padding: 10,
                border: "1px solid #ccc",
                borderRadius: 8,
              }}
            >
              <h3>{take.agent}</h3>
              <p style={{ whiteSpace: "pre-wrap" }}>{take.take}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
