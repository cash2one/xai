

#calss header
class _AGAIN():
	def __init__(self,): 
		self.name = "AGAIN"
		self.definitions = [u'one more time: ', u'back to the original place or condition: ', u'If something happens once again, it has already happened several times before: ', u'said after an unpleasant experience to show that you do not intend to do it again: ', u'If something happens yet again, it has already happened many times before: ', u'repeatedly: ', u'If you do something all over again, you start again from the beginning: ', u'in addition to the amount we know about or have mentioned already: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
