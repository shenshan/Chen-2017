from pipeline.ingest import ingest_meta_data, ingest_data
from pipeline import imaging


ingest_data.main()
imaging.RoiAnalyses.populate(suppress_errors=True, display_progress=True)
