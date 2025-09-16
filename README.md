# 🛫 Pipelines de Voos com Apache Beam e Google Cloud

Este repositório contém três scripts de processamento em batch utilizando [Apache Beam](https://beam.apache.org/) com diferentes combinações de serviços da Google Cloud: **Cloud Storage**, **BigQuery**, **Dataflow** e **DirectRunner**.

## 📂 Scripts

| Script                             | Runner        | Entrada       | Saída         |
|------------------------------------|---------------|---------------|---------------|
| `voos_batch_dataflow_bigquery.py`  | Dataflow      | Cloud Storage | BigQuery      |
| `voos_batch_dataflow_gcs.py`       | Dataflow      | Cloud Storage | Cloud Storage |
| `voos_batch_directrunner_gcs.py`   | DirectRunner  | Local         | Cloud Storage |

## 🔁 Fluxo de Dados

O diagrama do projeto representa três cenários:

1. **Execução Local (DirectRunner)**  
   - Leitura local e escrita no Cloud Storage via máquina local.

2. **Execução no Cloud com Dataflow (GCS → GCS)**  
   - Pipeline gerenciada no Dataflow, com entrada e saída em buckets do GCS.

3. **Execução no Cloud com Dataflow (GCS → BigQuery)**  
   - Entrada via GCS e persistência final em uma tabela do BigQuery.
