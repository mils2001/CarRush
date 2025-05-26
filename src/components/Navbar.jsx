import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-gray-800 p-4 shadow-md text-white flex justify-between">
      <h1 className="text-yellow-400 font-bold text-xl">CarRush</h1>
      <div className="space-x-4">
        <Link to="/" className="hover:text-yellow-400">Home</Link>
        <Link to="/about" className="hover:text-yellow-400">About</Link>
        <Link to="/cars" className="hover:text-yellow-400">Cars</Link>
        <Link to="/rent" className="hover:text-yellow-400">Rent</Link>
        <Link to="/payments" className="hover:text-yellow-400">Payments</Link>
      </div>
    </nav>
  );
}
