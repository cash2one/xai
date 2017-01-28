

#calss header
class _RETENTIVE():
	def __init__(self,): 
		self.name = "RETENTIVE"
		self.definitions = [u'If you have a retentive memory or brain, you can remember things easily.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
