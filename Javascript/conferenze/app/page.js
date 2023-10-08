import Link from "next/link";
import Navbar from "@components/Navbar";
import Footer from "@components/Footer";
import Feed from "@components/Feed";

// function format_date()

export default function Page() {
  // console.log(card);

  return (
    <>
      <Navbar />

      <main className="relative m-0 p-0">
        <Feed />
      </main>
      <Footer />
    </>
  );
}
