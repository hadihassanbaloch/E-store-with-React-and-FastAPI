import { Link } from 'react-router-dom';

function ProductCard({ product }) {
  return (
    <Link to={`/product/${product.id}`} className="card">
      <div className='image-container'>
        <img src={product.image} alt={product.name} width="150" className='product-image'/>
      </div>
      <h3>{product.name}</h3>
      <div className="price-footer">
       <div className='price-icons'>
          <span className='icon'>❤️</span>
          <span className='icon'>🛒</span>
        </div>
        <span className='price'>${product.price}</span>
      </div>

    </Link>
  );
}

export default ProductCard;
