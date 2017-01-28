

#calss header
class _BROKEN():
	def __init__(self,): 
		self.name = "BROKEN"
		self.definitions = [u'damaged, no longer able to work: ', u'suffering emotional pain that is so strong that it changes the way you live, usually as a result of an unpleasant event: ', u'interrupted or not continuous: ', u'destroyed or ended: ', u'(of a law, rule, or promise) not obeyed or not kept: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
