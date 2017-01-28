

#calss header
class _PROPORTIONAL():
	def __init__(self,): 
		self.name = "PROPORTIONAL"
		self.definitions = [u'If two amounts are proportional, they change at the same rate so that the relationship between them does not change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
