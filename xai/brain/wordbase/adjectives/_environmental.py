

#calss header
class _ENVIRONMENTAL():
	def __init__(self,): 
		self.name = "ENVIRONMENTAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
