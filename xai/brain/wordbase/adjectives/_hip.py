

#calss header
class _HIP():
	def __init__(self,): 
		self.name = "HIP"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
