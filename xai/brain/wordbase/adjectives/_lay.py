

#calss header
class _LAY():
	def __init__(self,): 
		self.name = "LAY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
