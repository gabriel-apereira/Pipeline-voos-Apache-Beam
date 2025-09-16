import apache_beam as beam
import os

serviceAccount = r'C:\Users\gabri\Desktop\Udemy\Apache GCP\dataflow-beam-voos-b1227139fe6e.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceAccount

p1 = beam.Pipeline()


class filtro(beam.DoFn):
    def process(self, record):
        if int(record[8]) > 0:
            return [record]


Tempo_Atrasos = (
    p1
    | "Importar Dados Atraso" >> beam.io.ReadFromText(r"C:\Users\gabri\Desktop\Udemy\Apache GCP\Inputs\voos_sample.csv", skip_header_lines=1)
    | "Separar por Vírgulas Atraso" >> beam.Map(lambda record: record.split(','))
    | "Pegar voos com atraso" >> beam.ParDo(filtro())
    | "Criar par atraso" >> beam.Map(lambda record: (record[4], int(record[8])))
    | "Somar por key" >> beam.CombinePerKey(sum)
)

Qtd_Atrasos = (
    p1
    | "Importar Dados" >> beam.io.ReadFromText(r"C:\Users\gabri\Desktop\Udemy\Apache GCP\Inputs\voos_sample.csv", skip_header_lines=1)
    | "Separar por Vírgulas Qtd" >> beam.Map(lambda record: record.split(','))
    | "Pegar voos com Qtd" >> beam.ParDo(filtro())
    | "Criar par Qtd" >> beam.Map(lambda record: (record[4], int(record[8])))
    | "Contar por key" >> beam.combiners.Count.PerKey()
)

tabela_atrasos = (
    {'Qtd_Atrasos': Qtd_Atrasos, 'Tempo_Atrasos': Tempo_Atrasos}
    | "Group By" >> beam.CoGroupByKey()
    | "Saida Para GCP" >> beam.io.WriteToText(r"gs://apache_beam_voos/saida/Voos_atrados_qtd.csv")
)

p1.run()
