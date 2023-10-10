export const getData = async () => {
  const res = await fetch("https://gdscdev.vercel.app/api");

  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  return res.json();
};
