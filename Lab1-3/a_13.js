const zlib = require('zlib');

const values = [
    'eJzzyc9Lyc8DAAgpAms=',
    'eJxzSi3KycwDAAfXAl0=',
    'eJzzSy1XiMwvygYADKUC8A=='
];

for (const value of values) {
    const compressed = Buffer.from(value, 'base64');
    const uncompressed = zlib.inflateSync(compressed);
    console.log(uncompressed.toString());
}
