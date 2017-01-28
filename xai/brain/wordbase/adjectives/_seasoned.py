

#calss header
class _SEASONED():
	def __init__(self,): 
		self.name = "SEASONED"
		self.definitions = [u'having a lot of experience of doing something and therefore knowing how to do it well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
