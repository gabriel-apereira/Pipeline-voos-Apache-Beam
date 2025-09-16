🛫 Pipelines de Voos com Apache Beam
Este repositório contém três scripts de processamento em batch usando Apache Beam com diferentes combinações de Cloud Storage, BigQuery e os runners Dataflow e DirectRunner.

📂 Scripts
Voos Batch Dataflow + BigQuery: lê do GCS e grava no BigQuery.

Voos Batch Dataflow + GCS: lê e grava no GCS via Dataflow.

Voos Batch DirectRunner + GCS: execução local com leitura e escrita no GCS.

🔁 Fluxo de Dados
Local → GCS

GCS → GCS (Dataflow)

GCS → BigQuery (Dataflow)
