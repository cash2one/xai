

#calss header
class _PRIMARY():
	def __init__(self,): 
		self.name = "PRIMARY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
