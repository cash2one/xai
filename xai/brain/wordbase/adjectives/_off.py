

#calss header
class _OFF():
	def __init__(self,): 
		self.name = "OFF"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
