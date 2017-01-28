

#calss header
class _AWAY():
	def __init__(self,): 
		self.name = "AWAY"
		self.definitions = [u'somewhere else, or to or in a different place, position, or situation: ', u'at a distance (of or from here): ', u'in or into the usual or a suitable place, especially one that can be closed: ', u'gradually until mostly or completely gone: ', u'in the future: ', u'continuously or repeatedly, or in a busy way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
