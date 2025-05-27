import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';

function ProductPage() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/products/${id}`)
      .then(response => setProduct(response.data))
      .catch(error => setError("Product not found"));
  }, [id]);

  if (error) return <h2>{error}</h2>;
  if (!product) return <h2>Loading...</h2>;

  return (
    <div className="container">
      <h1 className='product-name'>{product.name}</h1>
      <div className='product-image-container'>
        <img src={product.image} alt={product.name} className='product-page-image' />
      </div>
      <div className='product-description'>
        <p className='product-price'>Price: ${product.price}</p>
        <p className='description'>This is a great product with premium quality</p>
      </div>
      <button className='add-to-cart'>Add to cart</button>
    </div>
  );
}

export default ProductPage;
