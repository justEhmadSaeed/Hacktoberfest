"use client";
import { AnimatePresence, motion } from "framer-motion";
export const Pagewrapper = ({ children }) => {
  return (
    <>
      <AnimatePresence>
        <motion.div
          // initial={{ opacity: 0, y: 15 }}
          // animate={{ opacity: 1, y: 0 }}
          // exist={{ opacity: 0, y: 15 }}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ ease: "easeOut", duration: 0.55 }}
        >
          {children}
        </motion.div>
      </AnimatePresence>
    </>
  );
};
