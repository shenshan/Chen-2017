from pipeline.ingest import ingest_lookup, ingest_data
from pipeline import imaging

ingest_data.main()
imaging.RoiAnalyses.populate(suppress_errors=True, display_progress=True)
