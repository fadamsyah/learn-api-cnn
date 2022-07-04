#!/bin/bash
function close_port {
    kill $(lsof -t -i:8080)
    kill $(lsof -t -i:5000)
    kill $(lsof -t -i:5001)
}
trap close_port EXIT
close_port
conda activate api-cnn
python cnn-api.py &
python db-api.py &
streamlit run app.py --server.port 8080 &
wait
close_port