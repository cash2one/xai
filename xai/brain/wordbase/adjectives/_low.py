

#calss header
class _LOW():
	def __init__(self,): 
		self.name = "LOW"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
