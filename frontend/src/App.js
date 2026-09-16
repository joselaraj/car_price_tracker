import { useEffect, useState } from "react";
import axios from "axios";
import ListingCard from "./ListingCard";

function App() {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/listings/")
      .then(res => setListings(res.data));
  }, []);

  return (
    <div style={{ background: "#111", minHeight: "100vh", padding: "2rem" }}>
      <h1 style={{ color: "#fff" }}>Tracked Listings</h1>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: "1rem" }}>
        {listings.map(l => <ListingCard key={l.id} listing={l} />)}
      </div>
    </div>
  );
}

export default App;