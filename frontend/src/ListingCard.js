import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

function ListingCard({ listing }) {
  const dropped = listing.current_price < listing.first_seen_price;

  return (
    <div style={{ background: "#1e1e1e", borderRadius: 8, padding: "1rem", color: "#fff" }}>
      <h3>{listing.year} {listing.make} {listing.model}</h3>
      <p style={{ color: dropped ? "#4ade80" : "#fff" }}>
        ${listing.current_price.toLocaleString()}
        {dropped && ` (was $${listing.first_seen_price.toLocaleString()})`}
      </p>
      <ResponsiveContainer width="100%" height={100}>
        <LineChart data={listing.history}>
          <XAxis dataKey="recorded_at" hide />
          <YAxis hide domain={["auto", "auto"]} />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#4ade80" dot={false} />
        </LineChart>
      </ResponsiveContainer>
      <a href={listing.url} target="_blank" rel="noreferrer" style={{ color: "#60a5fa" }}>
        View listing →
      </a>
    </div>
  );
}

export default ListingCard;