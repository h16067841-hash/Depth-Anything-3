export interface Product {
  id: string;
  name: string;
  description: string;
  price: number;
  image: string;
  category: string;
  supplier: string;
  stock: number;
  shippingDays: number;
}

export const products: Product[] = [
  {
    id: '1',
    name: 'Ergonomic Standing Desk Converter',
    description: 'Transform your traditional desk into a height-adjustable standing workstation. Premium aluminum frame with smooth electric lift mechanism. Supports up to 35 lbs. Compatible with all desk sizes.',
    price: 599,
    image: '/images/desk-converter.jpg',
    category: 'Desks',
    supplier: 'ErgoTech Supplies',
    stock: 50,
    shippingDays: 3
  },
  {
    id: '2',
    name: 'Wireless Ergonomic Keyboard',
    description: 'Mechanical keyboard with ergonomic split design and adjustable tenting. Low-profile keys with tactile feedback. Bluetooth 5.0 connectivity with 3-month battery life.',
    price: 249,
    image: '/images/keyboard.jpg',
    category: 'Keyboards',
    supplier: 'TechErgo Inc.',
    stock: 100,
    shippingDays: 5
  },
  {
    id: '3',
    name: 'Vertical Mouse',
    description: 'Ambidextrous vertical mouse designed to reduce wrist strain. 1000 DPI optical sensor with programmable buttons. USB-C rechargeable with 2-month battery life.',
    price: 89,
    image: '/images/mouse.jpg',
    category: 'Mice',
    supplier: 'ComfortInput Ltd.',
    stock: 200,
    shippingDays: 4
  },
  {
    id: '4',
    name: 'Adjustable Monitor Arm',
    description: 'Dual monitor arm with gas-spring adjustment. Supports screens up to 32 inches and 20 lbs each. Full range of motion with cable management system.',
    price: 179,
    image: '/images/monitor-arm.jpg',
    category: 'Monitor Accessories',
    supplier: 'DisplayPro Solutions',
    stock: 75,
    shippingDays: 6
  },
  {
    id: '5',
    name: 'Ergonomic Office Chair',
    description: 'High-back mesh office chair with lumbar support and adjustable armrests. Breathable fabric with 360-degree swivel. Weight capacity: 300 lbs.',
    price: 449,
    image: '/images/office-chair.jpg',
    category: 'Chairs',
    supplier: 'ComfortSeating Co.',
    stock: 30,
    shippingDays: 7
  },
  {
    id: '6',
    name: 'Foot Rest with Massage',
    description: 'Adjustable foot rest with built-in massage rollers and heating element. Memory foam surface with anti-slip base. Remote control included.',
    price: 129,
    image: '/images/foot-rest.jpg',
    category: 'Foot Support',
    supplier: 'WellnessGear EU',
    stock: 150,
    shippingDays: 4
  },
  {
    id: '7',
    name: 'Laptop Stand with Cooling',
    description: 'Aluminum laptop stand with built-in cooling fans. Adjustable height and angle. Compatible with laptops up to 17 inches. USB-powered.',
    price: 79,
    image: '/images/laptop-stand.jpg',
    category: 'Laptop Accessories',
    supplier: 'CoolTech Accessories',
    stock: 120,
    shippingDays: 3
  },
  {
    id: '8',
    name: 'Ergonomic Wrist Rest',
    description: 'Gel-filled wrist rest with memory foam. Antimicrobial surface. Available in multiple sizes. Provides cushioning and support for extended typing sessions.',
    price: 39,
    image: '/images/wrist-rest.jpg',
    category: 'Wrist Support',
    supplier: 'ErgoComfort Supplies',
    stock: 300,
    shippingDays: 5
  },
  {
    id: '9',
    name: 'Standing Desk Mat',
    description: 'Anti-fatigue standing mat with gel cushioning. Beveled edges for safety. Water-resistant surface. Size: 24x36 inches.',
    price: 69,
    image: '/images/standing-mat.jpg',
    category: 'Floor Mats',
    supplier: 'FloorComfort Inc.',
    stock: 80,
    shippingDays: 6
  },
  {
    id: '10',
    name: 'Document Holder',
    description: 'Adjustable document holder with line guide. Reduces neck strain while reading. Magnetic base for easy attachment. Folds flat for storage.',
    price: 29,
    image: '/images/document-holder.jpg',
    category: 'Desk Accessories',
    supplier: 'OfficeErgo Tools',
    stock: 250,
    shippingDays: 4
  },
  {
    id: '11',
    name: 'Cable Management Tray',
    description: 'Under-desk cable management tray. Keeps wires organized and hidden. Adjustable width. Easy to install with included hardware.',
    price: 49,
    image: '/images/cable-tray.jpg',
    category: 'Cable Management',
    supplier: 'WireWise Solutions',
    stock: 180,
    shippingDays: 5
  },
  {
    id: '12',
    name: 'Ergonomic Pen Holder',
    description: 'Weighted pen holder designed for comfortable grip. Reduces hand fatigue. Magnetic base. Compatible with most pens and pencils.',
    price: 19,
    image: '/images/pen-holder.jpg',
    category: 'Desk Accessories',
    supplier: 'WriteEase Products',
    stock: 400,
    shippingDays: 3
  },
  {
    id: '13',
    name: 'Monitor Light Bar',
    description: 'LED light bar for monitors. Reduces eye strain with natural light spectrum. Adjustable brightness and color temperature. USB-powered.',
    price: 59,
    image: '/images/monitor-light.jpg',
    category: 'Lighting',
    supplier: 'BrightView Lighting',
    stock: 90,
    shippingDays: 4
  },
  {
    id: '14',
    name: 'Ergonomic Mouse Pad',
    description: 'Large mouse pad with wrist support. Smooth surface for precise tracking. Anti-slip base. Size: 12x10 inches.',
    price: 25,
    image: '/images/mouse-pad.jpg',
    category: 'Mouse Accessories',
    supplier: 'PrecisionInput Ltd.',
    stock: 220,
    shippingDays: 5
  },
  {
    id: '15',
    name: 'Desk Organizer with Phone Stand',
    description: 'Multi-compartment desk organizer with integrated phone stand. Keeps desk clutter-free. Modern design with cable management slots.',
    price: 45,
    image: '/images/desk-organizer.jpg',
    category: 'Desk Accessories',
    supplier: 'OrganizePro Office',
    stock: 160,
    shippingDays: 6
  },
  {
    id: '16',
    name: 'Ergonomic Headset Stand',
    description: 'Adjustable headset stand with cable management. Keeps headset off desk surface. Compatible with most headsets. Compact design.',
    price: 35,
    image: '/images/headset-stand.jpg',
    category: 'Headset Accessories',
    supplier: 'AudioErgo Solutions',
    stock: 140,
    shippingDays: 4
  },
  {
    id: '17',
    name: 'Lumbar Support Cushion',
    description: 'Memory foam lumbar support cushion. Adjustable strap for chairs. Provides lower back support. Machine washable cover.',
    price: 55,
    image: '/images/lumbar-cushion.jpg',
    category: 'Back Support',
    supplier: 'BackCare Essentials',
    stock: 110,
    shippingDays: 5
  },
  {
    id: '18',
    name: 'Ergonomic Notebook Stand',
    description: 'Adjustable notebook stand with cooling vents. Reduces heat buildup. Compatible with notebooks up to 15 inches. Foldable for portability.',
    price: 39,
    image: '/images/notebook-stand.jpg',
    category: 'Laptop Accessories',
    supplier: 'NoteCool Stands',
    stock: 190,
    shippingDays: 3
  },
  {
    id: '19',
    name: 'Desk Lamp with USB Charging',
    description: 'LED desk lamp with wireless charging pad. Adjustable arm and brightness. Touch controls. Provides focused task lighting.',
    price: 89,
    image: '/images/desk-lamp.jpg',
    category: 'Lighting',
    supplier: 'ChargeLight Solutions',
    stock: 70,
    shippingDays: 6
  },
  {
    id: '20',
    name: 'Ergonomic Gaming Chair',
    description: 'Premium gaming chair with ergonomic design. Adjustable height and recline. High-density foam cushions. Weight capacity: 330 lbs.',
    price: 399,
    image: '/images/gaming-chair.jpg',
    category: 'Chairs',
    supplier: 'GameComfort Seating',
    stock: 40,
    shippingDays: 7
  }
];

export const suppliers = [
  { name: 'ErgoTech Supplies', contact: 'orders@ergotech.com', region: 'US' },
  { name: 'TechErgo Inc.', contact: 'sales@techergo.com', region: 'US' },
  { name: 'ComfortInput Ltd.', contact: 'support@comfortinput.com', region: 'EU' },
  { name: 'DisplayPro Solutions', contact: 'info@displaypro.com', region: 'US' },
  { name: 'ComfortSeating Co.', contact: 'contact@comfortseating.com', region: 'US' },
  { name: 'WellnessGear EU', contact: 'eu@wellnessgear.com', region: 'EU' },
  { name: 'CoolTech Accessories', contact: 'sales@cooltech.com', region: 'US' },
  { name: 'ErgoComfort Supplies', contact: 'orders@ergocomfort.com', region: 'US' },
  { name: 'FloorComfort Inc.', contact: 'support@floorcomfort.com', region: 'US' },
  { name: 'OfficeErgo Tools', contact: 'info@officeergo.com', region: 'US' },
  { name: 'WireWise Solutions', contact: 'sales@wirewise.com', region: 'US' },
  { name: 'WriteEase Products', contact: 'contact@writeease.com', region: 'US' },
  { name: 'BrightView Lighting', contact: 'support@brightview.com', region: 'EU' },
  { name: 'PrecisionInput Ltd.', contact: 'info@precisioninput.com', region: 'US' },
  { name: 'OrganizePro Office', contact: 'sales@organizepro.com', region: 'US' },
  { name: 'AudioErgo Solutions', contact: 'contact@audioergo.com', region: 'EU' },
  { name: 'BackCare Essentials', contact: 'support@backcare.com', region: 'US' },
  { name: 'NoteCool Stands', contact: 'orders@notecool.com', region: 'US' },
  { name: 'ChargeLight Solutions', contact: 'info@chargelight.com', region: 'US' },
  { name: 'GameComfort Seating', contact: 'sales@gamecomfort.com', region: 'US' }
];