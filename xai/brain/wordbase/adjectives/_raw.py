

#calss header
class _RAW():
	def __init__(self,): 
		self.name = "RAW"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
