

#calss header
class _PRESBYTERIAN():
	def __init__(self,): 
		self.name = "PRESBYTERIAN"
		self.definitions = [u'relating or belonging to a Christian group that has members especially in Scotland and the US']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
