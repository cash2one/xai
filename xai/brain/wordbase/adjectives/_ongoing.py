

#calss header
class _ONGOING():
	def __init__(self,): 
		self.name = "ONGOING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
