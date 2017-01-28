

#calss header
class _WATERLOGGED():
	def __init__(self,): 
		self.name = "WATERLOGGED"
		self.definitions = [u'(of land) full of water and almost covered by a layer of it: ', u'(of a boat) full of water and therefore unable to keep moving or floating']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
