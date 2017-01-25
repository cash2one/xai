

#calss header
class _ELEMENTARY():
	def __init__(self,): 
		self.name = "ELEMENTARY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
