

#calss header
class _COMMON():
	def __init__(self,): 
		self.name = "COMMON"
		self.definitions = [u'the same in a lot of places or for a lot of people: ', u'the basic level of politeness that you expect from someone', u'a fact that everyone knows: ', u'belonging to or shared by two or more people, or things: ', u'If something is done for the common good, it is done to help everyone.', u'to act together with someone in order to achieve something: ', u'typical of a low social class: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
