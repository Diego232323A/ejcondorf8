const express = require("express");
const app = express();
const cors = require("cors");

app.use(cors());
app.use(express.json());

const router = express.Router();

router.post("/counter", function (req, res) {
  const text = req.body.text;
  const response = {
    words: text.trim().split(/\s+/).length,
    characters: text.length,
  };
  res.send(response);
});

app.use(router);

app.listen(7020, function () {
  console.log("Node server running on https://localhost:7020");
});
