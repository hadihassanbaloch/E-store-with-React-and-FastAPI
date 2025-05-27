import { useEffect, useState } from 'react';
import axios from 'axios';
import ProductCard from '../components/ProductCard';

function Home() {
  const [search, setSearch] = useState('');
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true); // loading state
  const [error, setError] = useState(null); // error handling

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/products')
      .then(response => {
        setProducts(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError("Error loading products");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="container">
      <h1 className='logo'>Adazon</h1>
      <input
        type="text"
        placeholder="Search products..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          padding: '10px',
          width: '100%',
          maxWidth: '300px',
          marginBottom: '20px',
          fontSize: '16px',
          borderRadius: '5px',
          border: '1px solid #ccc'
        }}
      />
      <div className="grid">
        {products
  .filter(product =>
          product.name.toLowerCase().includes(search.toLowerCase())
        )
        .map(product => (
          <ProductCard key={product.id} product={product} />
      ))}
      </div>
    </div>
  );
}

export default Home;
