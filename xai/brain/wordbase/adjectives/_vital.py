

#calss header
class _VITAL():
	def __init__(self,): 
		self.name = "VITAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
