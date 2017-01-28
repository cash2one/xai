

#calss header
class _SOLEMN():
	def __init__(self,): 
		self.name = "SOLEMN"
		self.definitions = [u'serious and without any humour: ', u'an agreement that you make in a serious way and expect to keep']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
