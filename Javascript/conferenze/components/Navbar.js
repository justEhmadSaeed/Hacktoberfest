import React from "react";
import Link from "next/link";

const Navbar = () => {
  return (
    <div className="flex fixed top-0 z-50 justify-center items-center w-full h-20 bg-slate-900 text-white px-8 mb-12">
      <div className="relative font-extrabold font-Poppins text-3xl text-center">
        <Link href="/">Conferenze</Link>
      </div>
    </div>
  );
};

export default Navbar;
