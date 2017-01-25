

#calss header
class _SILENT():
	def __init__(self,): 
		self.name = "SILENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
