import { MongoClient } from "mongodb";

const uri = process.env.COSMOS_MONGO_URI || "mongodb://cosmos-demo.mongo.cosmos.azure.com:10255/?ssl=true";
const username = process.env.COSMOS_MONGO_USERNAME || "atul";
const password = process.env.COSMOS_MONGO_PASSWORD || "ChangeMe123!";

const client = new MongoClient(uri, { auth: { username, password } });

async function main() {
  await client.connect();
  const db = client.db("iotdb");
  const readings = db.collection("readings");
  await readings.insertOne({ device: "sensor-001", temp: 26, ts: new Date() });
  const docs = await readings.find().limit(10).toArray();
  console.log(docs);
}

main()
  .catch((err) => {
    console.error(err);
    process.exitCode = 1;
  })
  .finally(() => client.close());
