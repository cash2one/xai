

#calss header
class _ORTHODOX():
	def __init__(self,): 
		self.name = "ORTHODOX"
		self.definitions = [u'(of beliefs, ideas, or activities) considered traditional, normal, and acceptable by most people: ', u'(of religious people) having more traditional beliefs than other people in the same religious group: ', u'a part of the Christian Church, with many members in Greece, Russia, and eastern Europe']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
