

#calss header
class _BACKWARDS():
	def __init__(self,): 
		self.name = "BACKWARDS"
		self.definitions = [u'towards the direction that is opposite to the one in which you are facing or opposite to the usual direction: ', u'returning to older and less effective ways: ', u'first in one direction and then in the opposite one: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
